import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('image')
def timeline(image): subprocess.run(['fls', '-r', image])
if __name__ == '__main__': cli()
