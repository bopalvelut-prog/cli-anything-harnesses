import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apple_pay running')
@cli.command()
def start(): click.echo('apple_pay started')
if __name__ == '__main__': cli()
