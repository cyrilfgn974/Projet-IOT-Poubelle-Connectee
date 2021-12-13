<script>
  let codeBarre;
  let nomProduit="";
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
  function onScanSuccess(decodedText, decodedResult) {
    console.log(`Code scanned = ${decodedText}`, decodedResult);
  }

  
</script>




<!-- <input on:change={launch} bind:value={codeBarre} />
<button on:click={launch}>Search product</button>
{#if launch}
  <p>name of the product: {nomProduit}</p>
  <p>link img produit : {src}</p>
  <img src={src} alt=''>
{/if} -->
<div class="header">
  <h1>Poubelle 2.0</h1>
</div>

<article class="input">
  <input on:change={launch} bind:value={codeBarre}/>
  <button on:click={launch}>Search product</button>
</article>
<article class="infos">
  {#if launch}
    {#if nomProduit}
      <h2>Vous avez scanné :</h2>
      <p>{nomProduit}</p>
    {/if}
    <img src={src} alt=''>
  {/if}
</article>


<style>
  
  .header{
    text-align: center;
    color: red;
    
  }
  .input{
    text-align: center;
  }
  .infos{
    text-align: center;
  }
</style>