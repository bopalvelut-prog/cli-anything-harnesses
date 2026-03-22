import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Fluent Forms forms')
if __name__ == '__main__': cli()
