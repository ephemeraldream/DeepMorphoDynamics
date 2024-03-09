<script>
  let imageId = '';
  let labels = null;
  let error = null;

  async function fetchLabels() {
    labels = null;
    error = null;

    try {
      const response = await fetch(`http://localhost:8000/api/methods/networks/gen_labels/${imageId}/`, {
        method: 'POST',
      });

      if (response.ok) {
        labels = await response.json();
      } else {
        error = `Error: ${response.status}`;
        console.error('Error fetching labels:', response);
      }
    } catch (err) {
      error = 'Network error';
      console.error('Network error:', err);
    }
  }
</script>

<div>
  <input type="text" bind:value={imageId} placeholder="Enter image ID" />
  <button on:click={fetchLabels}>Get Labels</button>
</div>

{#if labels}
  <div>
    <h3>Retrieved Labels:</h3>
    <pre>{JSON.stringify(labels, null, 2)}</pre>
  </div>
{/if}

{#if error}
  <div class="error">{error}</div>
{/if}