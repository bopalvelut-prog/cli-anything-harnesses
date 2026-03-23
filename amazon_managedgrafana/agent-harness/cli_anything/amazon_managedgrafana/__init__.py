import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_managedgrafana running')
@cli.command()
def start(): click.echo('amazon_managedgrafana started')
if __name__ == '__main__': cli()
