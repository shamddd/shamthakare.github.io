// Smooth Client-Side Page Transitions matching SvelteKit on shamulent.github.io
(function () {
  const cache = new Map();

  const supportedPages = ['index.html', 'publications.html', 'papers.html', 'teaching.html', 'bio.html', 'blog.html'];

  function normalize(path) {
    if (!path) return '';
    let p = path.split('?')[0].split('#')[0];
    if (p.endsWith('/')) p += 'index.html';
    const parts = p.split('/');
    return parts[parts.length - 1] || 'index.html';
  }

  function prefetch(url) {
    const file = normalize(url);
    if (!file || !supportedPages.includes(file) || cache.has(file)) return;
    fetch(url)
      .then(res => res.ok ? res.text() : null)
      .then(html => {
        if (html) cache.set(file, html);
      })
      .catch(() => {});
  }

  function updateNav(targetFile) {
    const navLinks = document.querySelectorAll('nav.svelte-1ggp7n1 a');
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      const linkFile = normalize(href);
      if (
        linkFile === targetFile ||
        (targetFile === 'index.html' && (href === '/' || href === 'index.html')) ||
        (targetFile === 'papers.html' && linkFile === 'publications.html')
      ) {
        link.classList.add('text-black');
      } else {
        link.classList.remove('text-black');
      }
    });
  }

  function render(doc, targetFile) {
    // 1. Update Title
    if (doc.title) {
      document.title = doc.title;
    }

    // 2. Update Header Subtitle (e.g., — Publications, — Teaching, — Bio)
    const oldH1 = document.querySelector('header h1');
    const newH1 = doc.querySelector('header h1');
    if (oldH1 && newH1) {
      oldH1.innerHTML = newH1.innerHTML;
    }

    // 3. Update Active Nav Link
    updateNav(targetFile);

    // 4. Update Main Content
    const oldMain = document.querySelector('main');
    const newMain = doc.querySelector('main');
    if (oldMain && newMain) {
      oldMain.innerHTML = newMain.innerHTML;
    }

    // 5. Scroll to top
    window.scrollTo({ top: 0, behavior: 'instant' });

    // 6. Re-render MathJax if present
    if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Queue) {
      window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
    }

    // 7. Reattach link listeners to newly swapped content
    attachListeners();
  }

  function navigateTo(url, push = true) {
    const targetFile = normalize(url);
    if (!supportedPages.includes(targetFile)) {
      window.location.href = url;
      return;
    }

    const applyPage = (html) => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');

      if (document.startViewTransition) {
        document.startViewTransition(() => {
          render(doc, targetFile);
        });
      } else {
        const main = document.querySelector('main');
        if (main) main.classList.add('page-transitioning');
        setTimeout(() => {
          render(doc, targetFile);
          if (main) main.classList.remove('page-transitioning');
        }, 120);
      }

      if (push) {
        window.history.pushState({ file: targetFile, url }, doc.title, url);
      }
    };

    if (cache.has(targetFile)) {
      applyPage(cache.get(targetFile));
    } else {
      fetch(url)
        .then(res => {
          if (!res.ok) throw new Error('Fetch failed');
          return res.text();
        })
        .then(html => {
          cache.set(targetFile, html);
          applyPage(html);
        })
        .catch(() => {
          window.location.href = url;
        });
    }
  }

  function attachListeners() {
    document.querySelectorAll('a').forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      if (href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) return;
      if (href.startsWith('http://') || href.startsWith('https://')) {
        // External link
        return;
      }
      if (href.endsWith('.pdf') || link.getAttribute('target') === '_blank') return;

      const norm = normalize(href);
      if (!supportedPages.includes(norm)) return;

      // Prefetch on hover and touch
      link.addEventListener('mouseenter', () => prefetch(href), { passive: true });
      link.addEventListener('touchstart', () => prefetch(href), { passive: true });

      link.onclick = (e) => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
        e.preventDefault();
        navigateTo(href);
      };
    });
  }

  window.addEventListener('popstate', (e) => {
    const url = (e.state && e.state.url) || window.location.pathname;
    navigateTo(url, false);
  });

  document.addEventListener('DOMContentLoaded', () => {
    const currentFile = normalize(window.location.pathname);
    cache.set(currentFile, document.documentElement.outerHTML);
    attachListeners();
  });
})();
