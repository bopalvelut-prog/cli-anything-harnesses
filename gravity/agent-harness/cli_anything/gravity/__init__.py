import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Gravity Forms forms')
@cli.command()
def entries(): click.echo('Gravity Forms entries')
if __name__ == '__main__': cli()
