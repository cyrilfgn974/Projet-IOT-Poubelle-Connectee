<script>
  let codeBarre;
  let nomProduit = "Nul";
  function getNameFromAPI(name) {
    fetch("./api/getproduit/" + codeBarre + ".json")
      .then((d) => d.text())
      .then((d) => (nomProduit = d));
  }
</script>

<input bind:value={codeBarre} />
<button on:click={getNameFromAPI}>Search product</button>
{#if getNameFromAPI}
  <p>name of the product: {nomProduit}</p>
{/if}
