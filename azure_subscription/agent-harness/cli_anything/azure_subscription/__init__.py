import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_subscription running')
@cli.command()
def start(): click.echo('azure_subscription started')
if __name__ == '__main__': cli()
