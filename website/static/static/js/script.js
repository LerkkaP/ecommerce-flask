document.addEventListener("DOMContentLoaded", function () {
  const flashes = document.querySelectorAll(
    ".flashes .error, .flashes .success"
  );

  flashes.forEach(function (flash) {
    setTimeout(function () {
      flash.style.display = "none";
    }, 5000);
  });

  const searchForm = document.getElementById("searchForm");
  const searchResults = document.getElementById("searchResults");

  searchForm.addEventListener("input", function () {
    const query = this.elements["search"].value;
    performSearch(query);
  });

  let currentSearch = null;

  function performSearch(query) {
    if (currentSearch) {
      currentSearch.abort();
    }

    currentSearch = new AbortController();
    const { signal } = currentSearch;

    if (query.trim() !== "") {
      fetch(`/search?search=${query}`, { signal })
        .then((response) => response.json())
        .then((data) => {
          if (data.watches.length > 0) {
            displayResults(data.watches);
            searchResults.style.display = "block";
          } else {
            displayNoResultsMessage();
          }
        })
        .catch((error) => {
          if (error.name !== "AbortError") {
            throw error;
          }
        });
    } else {
      searchResults.style.display = "none";
      searchResults.innerHTML = "";
    }
  }

  function displayNoResultsMessage() {
    const searchResults = document.querySelector(".search-results");
    searchResults.innerHTML = '<div class="no-results">No results found.</div>';
    searchResults.style.display = "block";
  }

  function displayResults(watches) {
    searchResults.innerHTML = "";
    for (const watch of watches) {
      console.log(watch);
      const watchItem = document.createElement("div");
      watchItem.innerHTML = `
          <a href="/watch/${watch.id}">
            ${watch.brand} ${watch.model} ${watch.price} €
          </a>
        `;
      searchResults.appendChild(watchItem);
    }
  }
});
