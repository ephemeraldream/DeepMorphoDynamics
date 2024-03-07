<script>
	import {onMount} from 'svelte';
	let imageUrl = '';
	onMount(async () => {
		const response = await fetch('http://localhost:8000/api/images/1/');
		const data = await response.json();
		imageUrl = data.image
	});


</script>

<main>
	<h1>Hello Ivan!</h1>
	{#if imageUrl}
		<img src="{imageUrl}" alt="Image from Django" />
		{:else}
		<p>Loading image..</p>
	{/if}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>