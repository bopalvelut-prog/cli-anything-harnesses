
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
@click.argument('output')
@click.option('--crf', default=23)
def convert(input, output, crf):
    subprocess.run(['ffmpeg', '-i', input, '-crf', str(crf), '-preset', 'medium', output])
    click.echo(f'Converted: {output}')
@cli.command()
@click.argument('input')
def info(input):
    subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_name,width,height', '-of', 'json', input])
if __name__ == '__main__': cli()
