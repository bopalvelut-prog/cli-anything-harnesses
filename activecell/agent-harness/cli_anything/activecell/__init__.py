import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('activecell running')
@cli.command()
def start(): click.echo('activecell started')
if __name__ == '__main__': cli()
