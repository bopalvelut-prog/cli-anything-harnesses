import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('master running')
@cli.command()
def start(): click.echo('master started')
if __name__ == '__main__': cli()
