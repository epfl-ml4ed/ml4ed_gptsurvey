<script>
    import { _ } from "svelte-i18n";
    import CheckmarkOutline from "carbon-icons-svelte/lib/CheckmarkOutline.svelte";
</script>

<h1 id="title">{$_("pagethanks_title")}</h1>

<div id="icon_container">
    <CheckmarkOutline size={127} />
</div>

<p>{$_("pagethanks_txt")}</p>

<style>
    #title {
        margin-top: 0px;
        margin-bottom: 8px;
        text-align: center;
    }

    p {
        white-space: pre-line;
        text-align: center;
        font-size: 1.5em;
    }

    #icon_container {
        margin-top: 32px;
        margin-bottom: 32px;
        text-align: center;
        color: #0f62fe;
    }
</style>
