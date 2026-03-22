import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Ninja Forms forms')
@cli.command()
def submissions(): click.echo('Ninja Forms submissions')
if __name__ == '__main__': cli()
