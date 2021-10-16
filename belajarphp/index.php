<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Belajar PHP</title>
</head>

<body>
    <H2>Daftar Nama Peserta </H2>
    <table> border="2" cellspacing="0" cellpadding="4"</table>

        <tr>
            <th>No.</th>
            <th>Nama Peserta</th>
        </tr>
    <?php for ($i = 1; $i <= 10; $i++) { ?>
            <tr>
                <td><?= $i; ?>.</td>
                <td>Nama Peserta <?= $i; ?></td>
            </tr>
    <?php } ?>
</body>

</html>