import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hall running')
@cli.command()
def start(): click.echo('hall started')
if __name__ == '__main__': cli()
