import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('darkstat running')
@cli.command()
def start(): click.echo('darkstat started')
if __name__ == '__main__': cli()
