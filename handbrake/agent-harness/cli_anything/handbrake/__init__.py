
import click, subprocess, json

@click.group()
def cli(): pass

@cli.command()
@click.argument('input')
@click.argument('output')
@click.option('-f', '--format', default='mp4')
@click.option('-e', '--encoder', default='x264')
@click.option('-b', '--bitrate', default='2000')
def encode(input, output, format, encoder, bitrate):
    cmd = ['HandBrakeCLI', '-i', input, '-o', output, '-f', format, '-e', encoder, '-b', bitrate]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        click.echo(f'Encoded: {output}')
    else:
        click.echo(f'Error: {result.stderr}')

@cli.command()
@click.option('--json', 'as_json', is_flag=True)
def presets(as_json):
    p = ['Fast 1080p30', 'Fast 720p30', 'Very Fast 1080p30']
    if as_json:
        click.echo(json.dumps({'presets': p}))
    else:
        for x in p: click.echo(x)

if __name__ == '__main__':
    cli()
