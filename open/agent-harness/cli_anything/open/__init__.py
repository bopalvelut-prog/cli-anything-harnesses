import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('open running')
@cli.command()
def start(): click.echo('open started')
if __name__ == '__main__': cli()
