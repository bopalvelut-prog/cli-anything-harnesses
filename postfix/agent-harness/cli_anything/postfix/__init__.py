import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Postfix running')
@cli.command()
def queue(): click.echo('Postfix queue')
if __name__ == '__main__': cli()
