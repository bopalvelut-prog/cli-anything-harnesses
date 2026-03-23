import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('warning running')
@cli.command()
def start(): click.echo('warning started')
if __name__ == '__main__': cli()
