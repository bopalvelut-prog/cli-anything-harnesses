import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('privacy running')
@cli.command()
def start(): click.echo('privacy started')
if __name__ == '__main__': cli()
