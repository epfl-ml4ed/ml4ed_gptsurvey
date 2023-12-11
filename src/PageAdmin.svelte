<script>
    import { _ } from "svelte-i18n";
    import { Dropdown } from "carbon-components-svelte";
    import { FileUploaderDropContainer } from "carbon-components-svelte";
    import { FileUploaderItem } from "carbon-components-svelte";
    import { PasswordInput } from "carbon-components-svelte";
    import { Button } from "carbon-components-svelte";
    import WarningAlt from "carbon-icons-svelte/lib/WarningAlt.svelte";
    import CloudUpload from "carbon-icons-svelte/lib/CloudUpload.svelte";

    let courseID = null;
    let files = [];
    let upload_admin_key = "";
    let server_msg = "";

    $: console.log(files);

    let courses_items = [
        { id: null, text: " " },
        {
            id: "BIO-210",
            text: "BIO-210: Applied software engineering for life sciences",
        },
        {
            id: "CS-101",
            text: "CS-101: Advanced information, computation, communication I",
        },
        {
            id: "CS-119(d)",
            text: "CS-119(d): Information, calcul, communication (Math)",
        },
        {
            id: "CS-119(g)",
            text: "CS-119(g): Information, calcul, communication (SV)",
        },
        {
            id: "CS-119(h)",
            text: "CS-119(h): Information, calcul, communication (GC)",
        },
        { id: "CS-401", text: "CS-401: Applied data analysis" },
        {
            id: "CS-431",
            text: "CS-431: Introduction to natural language processing",
        },
        { id: "CS-433", text: "CS-433: Machine learning" },
        { id: "CS-502", text: "CS-502: Deep learning in biomedicine" },
        { id: "MATH-101(c)###Exercice14", text: "MATH-101(c): Analysis I, Task: Exercice 14" },
        { id: "MATH-101(c)###Exercice15", text: "MATH-101(c): Analysis I, Task: Exercice 15" },
        { id: "MATH-101(ol)###Exercice14", text: "MATH-101(ol): Analyse I (online), Task: Exercice 14" },
        { id: "MATH-101(ol)###Exercice15", text: "MATH-101(ol): Analyse I (online), Task: Exercice 15" },
    ];

    // Send results to server
    async function send_csv() {
        let data = new FormData();
        for (let file of files) {
            data.append("files", file);
        }
        fetch(
            `${import.meta.env.VITE_BACKEND}update_csv?` +
                new URLSearchParams({
                    access_key: upload_admin_key,
                    courseID: courseID,
                }),
            {
                method: "POST",
                body: data,
            }
        )
            .then((response) => response.text())
            .then((text) => {
                server_msg = "SERVER MSG : " + text;
            })
            .catch((error) => {
                server_msg = "ERROR: " + error;
            });
    }
</script>

{#if server_msg == ""}
    <h1 id="title">Course CSV upload</h1>
    <p><WarningAlt size={32} /></p>
    <p>
        Uploading a csv will overwrite the current server csv. The name of the
        uploaded csv does not matter, it will replace the csv for the course
        indicated in the menu below.
    </p>
    <Dropdown
        direction="bottom"
        titleText="COURSE"
        items={courses_items}
        bind:selectedId={courseID}
        invalidText={$_("pageconsent_course_invalid")}
        invalid={courseID == null}
    />
    {#if courseID}
        <p>Backend database courseID :</p>
        <p><b>{courseID}</b></p>
    {/if}
    <div style="margin-top: 32px">
        <FileUploaderDropContainer
            labelText="Drag and drop a .csv file here or click to upload"
            accept={[".csv"]}
            bind:files
        />
    </div>
    <div style="margin-top: 16px; margin-bottom: 32px">
        {#each files as f}
            <FileUploaderItem id={f.id} name={f.name} status="complete" />
        {/each}
    </div>
    <PasswordInput
        labelText="PASSWORD"
        placeholder="Enter upload admin key"
        invalidText="Please enter key"
        invalid={upload_admin_key == ""}
        bind:value={upload_admin_key}
    />
    <div style="margin-top: 32px;">
        <Button on:click={send_csv} icon={CloudUpload}>Update csv</Button>
    </div>
{:else}
    <p>{server_msg}</p>
{/if}

<style>
    p {
        margin: 10px;
        text-align: center;
    }
    b {
        font-family:Consolas,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New, monospace;
    }
</style>
