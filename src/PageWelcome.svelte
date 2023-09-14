<script>
    import { _ } from "svelte-i18n";
</script>

<h1 id="title">{$_("pagewelcome_title")}</h1>
<p>{$_("pagewelcome_intro")}</p>

<style>
    #title {
        margin-top: 8px;
        margin-bottom: 8px;
        text-align: center;
    }

    p {
        white-space: pre-line;
        text-align: justify;
    }
</style>
