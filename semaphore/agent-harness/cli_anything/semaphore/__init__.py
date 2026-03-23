import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('semaphore running')
@cli.command()
def start(): click.echo('semaphore started')
if __name__ == '__main__': cli()
