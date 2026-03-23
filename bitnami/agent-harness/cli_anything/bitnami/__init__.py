import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bitnami running')
@cli.command()
def start(): click.echo('bitnami started')
if __name__ == '__main__': cli()
