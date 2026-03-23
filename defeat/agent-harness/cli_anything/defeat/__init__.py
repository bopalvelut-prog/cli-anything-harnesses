import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('defeat running')
@cli.command()
def start(): click.echo('defeat started')
if __name__ == '__main__': cli()
