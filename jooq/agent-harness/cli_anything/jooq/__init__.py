import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jooq running')
@cli.command()
def start(): click.echo('jooq started')
if __name__ == '__main__': cli()
