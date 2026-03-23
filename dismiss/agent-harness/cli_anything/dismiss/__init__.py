import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dismiss running')
@cli.command()
def start(): click.echo('dismiss started')
if __name__ == '__main__': cli()
