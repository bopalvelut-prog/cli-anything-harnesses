import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('codefresh running')
@cli.command()
def start(): click.echo('codefresh started')
if __name__ == '__main__': cli()
