import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prince running')
@cli.command()
def start(): click.echo('prince started')
if __name__ == '__main__': cli()
