import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apigee running')
@cli.command()
def start(): click.echo('apigee started')
if __name__ == '__main__': cli()
