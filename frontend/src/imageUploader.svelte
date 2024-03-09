<script>
  import { onMount } from 'svelte';

  let subgroupID = '';

  async function uploadImage(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    formData.append('subgroup_id', subgroupID);

    try {
      const response = await fetch('http://localhost:8000/api/combined_data/images/', {
        method: 'POST',
        body: formData,
      });
      if (response.ok) {
        const data = await response.json();
        console.log('Image uploaded successfully:', data);
      } else {
        console.error('Error uploading image:', response);
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  }
</script>

<form on:submit|preventDefault={uploadImage}>
  <input type="file" name="image" accept="image/*" />
  <input type="text" bind:value={subgroupID} placeholder="Subgroup ID" />
  <button type="submit">Upload Image</button>
</form>