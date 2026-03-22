import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('image')
def info(image): subprocess.run(['vol', '-f', image, 'windows.info'])
@cli.command()
@click.argument('image')
def pslist(image): subprocess.run(['vol', '-f', image, 'windows.pslist'])
if __name__ == '__main__': cli()
