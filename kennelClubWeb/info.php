<?php
echo "<h1>Test del servidor web</h1>";
echo "<p>Si puedes ver esto, el servidor web está funcionando.</p>";
echo "<p>Fecha y hora: " . date('Y-m-d H:i:s') . "</p>";
echo "<p>Directorio actual: " . __DIR__ . "</p>";
echo "<p>Archivos en el directorio:</p>";
echo "<ul>";
$files = scandir(__DIR__);
foreach($files as $file) {
    if($file != '.' && $file != '..') {
        echo "<li>$file</li>";
    }
}
echo "</ul>";
?> 