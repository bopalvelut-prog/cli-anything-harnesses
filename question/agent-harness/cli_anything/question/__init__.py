import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('question running')
@cli.command()
def start(): click.echo('question started')
if __name__ == '__main__': cli()
