import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['bundle', 'exec', 'jekyll', 'serve'])
@cli.command()
def build(): subprocess.run(['bundle', 'exec', 'jekyll', 'build'])
@cli.command()
@click.argument('name')
def new(name): subprocess.run(['bundle', 'exec', 'jekyll', 'new', name])
if __name__ == '__main__': cli()
