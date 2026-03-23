import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('microservices running')
@cli.command()
def start(): click.echo('microservices started')
if __name__ == '__main__': cli()
