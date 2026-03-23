import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('replica running')
@cli.command()
def start(): click.echo('replica started')
if __name__ == '__main__': cli()
