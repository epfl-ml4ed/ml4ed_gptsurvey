<script>
    import { _ } from "svelte-i18n";

    export let bottom_bar_next_enabled;
    export let sciperID;
</script>

<h1 id="title">{$_("pagewelcome_title")}</h1>
<p>{$_("pagewelcome_intro")}</p>

<style>
    #title {
        margin-top: 0px;
        margin-bottom: 32px;
        text-align: center;
    }

    p {
        white-space: pre-line;
        text-align: justify;
    }
</style>
