<script>
    import {onMount} from 'svelte';

    let imageUrl = '';
    let imageFile;
    onMount(async () => {
        const response = await fetch('http://localhost:8000/api/images/6/');
        const data = await response.json();
        imageUrl = data.image
    });

    async function uploadImage(event) {
        const file = event.target.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('image', file);

            try {
                const response = await fetch('http://localhost:8000/api/images/', {
                    method: 'POST',
                    body: formData,
                    // If you're using authentication, you may need to add headers for the token
                    // headers: {
                    //   'Authorization': 'Token your_token_here',
                    // },
                });

                if (response.ok) {
                    const data = await response.json();
                    console.log('Image uploaded successfully:', data);
                    // Handle the response data as needed
                } else {
                    console.error('Upload failed:', response.status, response.statusText);
                }
            } catch (error) {
                console.error('Error uploading image:', error);
            }
        }
    }

</script>

<main>
    <head>
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1.0" name="viewport">
        <title>MorphoDynamics</title>
        <link href="style.css" rel="stylesheet">
    </head>
    <body>
    <div class="label-studio-container">
        <header>
            <h1>MorphoDynamics </h1>
        </header>
        <main>
            <aside>
                <ul>
                    <li><a href="#">Project 1</a></li>
                    <li><a href="#">Project 2</a></li>
                    <li><a href="#">Settings</a></li>
                </ul>
                <div class="tools">
                    <button>Add Task</button>
                    <button>Save Changes</button>
                    <button>Discard Changes</button>
                </div>
            </aside>
            <section class="content-area">
                <img alt="Image to be annotated" src="image.jpg"/>
                <div class="annotations">
                    <label for="label-1">Class:</label>
                    <select id="label-1">
                        <option value="">Select class...</option>
                        <option value="cat">Cat</option>
                        <option value="dog">Dog</option>
                        <option value="bird">Bird</option>
                    </select>
                    <button>Add Annotation</button>
                </div>
            </section>
        </main>
    </div>
    </body>
</main>

<style>

</style>