import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('psalm running')
@cli.command()
def start(): click.echo('psalm started')
if __name__ == '__main__': cli()
