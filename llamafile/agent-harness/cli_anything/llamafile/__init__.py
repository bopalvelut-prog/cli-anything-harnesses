import click
@click.group()
def cli(): pass
@cli.command()
def run(): click.echo('Llamafile run')
@cli.command()
def models(): click.echo('Llamafile models')
if __name__ == '__main__': cli()
