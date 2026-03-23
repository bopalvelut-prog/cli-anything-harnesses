import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lawyer running')
@cli.command()
def start(): click.echo('lawyer started')
if __name__ == '__main__': cli()
