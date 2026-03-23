import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('elect running')
@cli.command()
def start(): click.echo('elect started')
if __name__ == '__main__': cli()
