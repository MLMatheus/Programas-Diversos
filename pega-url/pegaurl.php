<?php
    $url = $_GET['url'];

    $pagina = file_get_contents($url);

    echo $pagina;
?>