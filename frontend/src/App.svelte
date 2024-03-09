<script>
    import {onMount} from 'svelte';
    import './style.css';
    import ImageUploader from './imageUploader.svelte';
    import LabelFetcher from "./LabelFetcher.svelte";

    let imageUrl = '';
    let imageFile;
    let imageSrc;
    let datA;
    onMount(async () => {
        const response = await fetch('http://localhost:8000/api/combined_data/well_timeline_frame/'+ 500);
        datA = await response.json();
        datA = datA.wtf_frame
        imageSrc = `data:image/bmp;base64,${datA}`;
    });






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
                    <li><a href="#">TODO 1</a></li>
                    <li><a href="#">TODO 2</a></li>
                    <li><a href="#">Settings</a></li>
                </ul>
                <div class="tools">
                    <button>Add Task</button>
                    <button>Save Changes</button>
                    <button>Discard Changes</button>
                </div>
            </aside>
            <section class="content-area">
                <img src={imageSrc} alt="Image to be annotated"/>
                <div class="annotations">
                    <label for="label-1">TODO:</label>
                    <select id="label-1">
                        <option value="">Select class...</option>
                        <option value="cat">Cat</option>
                        <option value="dog">Dog</option>
                        <option value="bird">Bird</option>
                    </select>
                    <button>Add Annotation</button>
                    <ImageUploader/>
                    <LabelFetcher/>
                    ### TODO

                </div>
            </section>
        </main>
    </div>
    </body>
</main>

<style>

</style>