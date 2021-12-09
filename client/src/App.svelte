<script>


  let codeBarre;
  let nomProduit;
  let src;
  function launch() {
    getNameFromAPI();
    getImageFromAPI();

  }
  function getNameFromAPI() {
    fetch("./api/getproduitname/" + codeBarre + ".json")
      .then((d) => d.text())
      .then((d) => (nomProduit = d))
  }
  function getImageFromAPI() {
    fetch("./api/getproduitimage/" + codeBarre + ".json")
      .then((d) => d.text())
      .then((d) => (src = d))
  }

</script>

<input bind:value={codeBarre} />
<button on:click={launch}>Search product</button>
{#if launch}
  <p>name of the product: {nomProduit}</p>
  <p>link img produit : {src}</p>
  <img src={src} alt=''>

{/if}
