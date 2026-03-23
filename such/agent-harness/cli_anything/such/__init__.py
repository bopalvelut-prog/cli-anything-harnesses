import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('such running')
@cli.command()
def start(): click.echo('such started')
if __name__ == '__main__': cli()
