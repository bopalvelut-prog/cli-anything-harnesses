import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('saga running')
@cli.command()
def start(): click.echo('saga started')
if __name__ == '__main__': cli()
